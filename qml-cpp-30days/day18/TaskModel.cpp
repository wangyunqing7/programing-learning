#include "TaskModel.h"

#include <QDateTime>
#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QStandardPaths>

TaskModel::TaskModel(QObject *parent)
    : QAbstractListModel(parent)
{
    seed();
    rebuildVisibleRows();
}

int TaskModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid()) {
        return 0;
    }
    return m_visibleRows.size();
}

QVariant TaskModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid()) {
        return {};
    }

    const int sourceRow = sourceRowForVisibleRow(index.row());
    if (sourceRow < 0) {
        return {};
    }

    const Task &task = m_tasks.at(sourceRow);
    switch (role) {
    case TitleRole:
        return task.title;
    case NoteRole:
        return task.note;
    case CategoryRole:
        return task.category;
    case DoneRole:
        return task.done;
    case CreatedAtRole:
        return task.createdAt;
    default:
        return {};
    }
}

QHash<int, QByteArray> TaskModel::roleNames() const
{
    return {
        {TitleRole, "title"},
        {NoteRole, "note"},
        {CategoryRole, "category"},
        {DoneRole, "done"},
        {CreatedAtRole, "createdAt"}
    };
}

QString TaskModel::filterText() const
{
    return m_filterText;
}

void TaskModel::setFilterText(const QString &text)
{
    if (m_filterText == text) {
        return;
    }
    m_filterText = text;
    rebuildVisibleRows();
    emit filterChanged();
    emit countChanged();
}

QString TaskModel::filterCategory() const
{
    return m_filterCategory;
}

void TaskModel::setFilterCategory(const QString &category)
{
    if (m_filterCategory == category) {
        return;
    }
    m_filterCategory = category;
    rebuildVisibleRows();
    emit filterChanged();
    emit countChanged();
}

int TaskModel::totalCount() const
{
    return m_tasks.size();
}

int TaskModel::visibleCount() const
{
    return m_visibleRows.size();
}

int TaskModel::completedCount() const
{
    int count = 0;
    for (const Task &task : m_tasks) {
        if (task.done) {
            ++count;
        }
    }
    return count;
}

QVariantMap TaskModel::get(int row) const
{
    const int sourceRow = sourceRowForVisibleRow(row);
    if (sourceRow < 0) {
        return {};
    }
    const Task &task = m_tasks.at(sourceRow);
    return {
        {QStringLiteral("title"), task.title},
        {QStringLiteral("note"), task.note},
        {QStringLiteral("category"), task.category},
        {QStringLiteral("done"), task.done},
        {QStringLiteral("createdAt"), task.createdAt}
    };
}

void TaskModel::addTask(const QString &title, const QString &note, const QString &category)
{
    const QString cleanTitle = title.trimmed();
    if (cleanTitle.isEmpty()) {
        return;
    }

    Task task;
    task.title = cleanTitle;
    task.note = note.trimmed();
    task.category = category.trimmed().isEmpty() ? QStringLiteral("默认") : category.trimmed();
    task.done = false;
    task.createdAt = QDateTime::currentDateTime().toString(Qt::ISODate);

    m_tasks.append(task);
    rebuildVisibleRows();
    emit countChanged();
}

void TaskModel::removeTask(int row)
{
    const int sourceRow = sourceRowForVisibleRow(row);
    if (sourceRow < 0) {
        return;
    }
    m_tasks.removeAt(sourceRow);
    rebuildVisibleRows();
    emit countChanged();
}

void TaskModel::updateTask(int row, const QString &title, const QString &note, const QString &category)
{
    const int sourceRow = sourceRowForVisibleRow(row);
    if (sourceRow < 0 || title.trimmed().isEmpty()) {
        return;
    }
    Task &task = m_tasks[sourceRow];
    task.title = title.trimmed();
    task.note = note.trimmed();
    task.category = category.trimmed().isEmpty() ? QStringLiteral("默认") : category.trimmed();
    rebuildVisibleRows();
    emit countChanged();
}

void TaskModel::toggleDone(int row)
{
    const int sourceRow = sourceRowForVisibleRow(row);
    if (sourceRow < 0) {
        return;
    }
    m_tasks[sourceRow].done = !m_tasks[sourceRow].done;
    const QModelIndex changed = index(row, 0);
    emit dataChanged(changed, changed, {DoneRole});
    emit countChanged();
}

void TaskModel::clearCompleted()
{
    for (int i = m_tasks.size() - 1; i >= 0; --i) {
        if (m_tasks.at(i).done) {
            m_tasks.removeAt(i);
        }
    }
    rebuildVisibleRows();
    emit countChanged();
}

bool TaskModel::save() const
{
    const QString path = storagePath();
    QDir().mkpath(QFileInfo(path).absolutePath());

    QJsonArray array;
    for (const Task &task : m_tasks) {
        array.append(toJson(task));
    }

    QFile file(path);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
        return false;
    }
    file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
    return true;
}

bool TaskModel::load()
{
    QFile file(storagePath());
    if (!file.exists()) {
        return save();
    }
    if (!file.open(QIODevice::ReadOnly)) {
        return false;
    }

    const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
    QVector<Task> loaded;
    for (const QJsonValue &value : document.array()) {
        loaded.append(fromJson(value.toObject()));
    }
    if (!loaded.isEmpty()) {
        m_tasks = loaded;
        rebuildVisibleRows();
        emit countChanged();
    }
    return true;
}

bool TaskModel::exportTo(const QString &fileName) const
{
    const QString path = documentPath(fileName.trimmed().isEmpty()
        ? QStringLiteral("qml-cpp-tasks-export.json")
        : fileName.trimmed());
    QDir().mkpath(QFileInfo(path).absolutePath());

    QJsonArray array;
    for (const Task &task : m_tasks) {
        array.append(toJson(task));
    }

    QFile file(path);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
        return false;
    }
    file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
    return true;
}

bool TaskModel::importFrom(const QString &fileName)
{
    const QString path = documentPath(fileName.trimmed().isEmpty()
        ? QStringLiteral("qml-cpp-tasks-export.json")
        : fileName.trimmed());
    QFile file(path);
    if (!file.open(QIODevice::ReadOnly)) {
        return false;
    }

    const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
    QVector<Task> imported;
    for (const QJsonValue &value : document.array()) {
        imported.append(fromJson(value.toObject()));
    }
    if (imported.isEmpty()) {
        return false;
    }
    m_tasks = imported;
    rebuildVisibleRows();
    emit countChanged();
    return true;
}

void TaskModel::seed()
{
    m_tasks = {
        {QStringLiteral("建立 QML + C++ App 框架"), QStringLiteral("界面由 QML 负责，数据由 C++ 模型负责。"), QStringLiteral("学习"), false, QDateTime::currentDateTime().toString(Qt::ISODate)},
        {QStringLiteral("实现任务增删改查"), QStringLiteral("通过 Q_INVOKABLE 暴露方法给 QML。"), QStringLiteral("功能"), false, QDateTime::currentDateTime().toString(Qt::ISODate)},
        {QStringLiteral("保存到 JSON 文件"), QStringLiteral("用 QJsonDocument 进行本地持久化。"), QStringLiteral("数据"), true, QDateTime::currentDateTime().toString(Qt::ISODate)}
    };
}

void TaskModel::rebuildVisibleRows()
{
    beginResetModel();
    m_visibleRows.clear();
    for (int i = 0; i < m_tasks.size(); ++i) {
        const Task &task = m_tasks.at(i);
        const bool textMatches = m_filterText.trimmed().isEmpty()
            || task.title.contains(m_filterText, Qt::CaseInsensitive)
            || task.note.contains(m_filterText, Qt::CaseInsensitive);
        const bool categoryMatches = m_filterCategory.trimmed().isEmpty()
            || m_filterCategory == QStringLiteral("全部")
            || task.category.compare(m_filterCategory, Qt::CaseInsensitive) == 0;
        if (textMatches && categoryMatches) {
            m_visibleRows.append(i);
        }
    }
    endResetModel();
}

int TaskModel::sourceRowForVisibleRow(int row) const
{
    if (row < 0 || row >= m_visibleRows.size()) {
        return -1;
    }
    return m_visibleRows.at(row);
}

QString TaskModel::storagePath() const
{
    return QStandardPaths::writableLocation(QStandardPaths::AppDataLocation)
        + QStringLiteral("/tasks.json");
}

QString TaskModel::documentPath(const QString &fileName) const
{
    QFileInfo info(fileName);
    if (info.isAbsolute()) {
        return fileName;
    }
    return QStandardPaths::writableLocation(QStandardPaths::DocumentsLocation)
        + QStringLiteral("/") + fileName;
}

QJsonObject TaskModel::toJson(const Task &task) const
{
    return {
        {QStringLiteral("title"), task.title},
        {QStringLiteral("note"), task.note},
        {QStringLiteral("category"), task.category},
        {QStringLiteral("done"), task.done},
        {QStringLiteral("createdAt"), task.createdAt}
    };
}

TaskModel::Task TaskModel::fromJson(const QJsonObject &object) const
{
    Task task;
    task.title = object.value(QStringLiteral("title")).toString();
    task.note = object.value(QStringLiteral("note")).toString();
    task.category = object.value(QStringLiteral("category")).toString(QStringLiteral("默认"));
    task.done = object.value(QStringLiteral("done")).toBool(false);
    task.createdAt = object.value(QStringLiteral("createdAt")).toString(QDateTime::currentDateTime().toString(Qt::ISODate));
    return task;
}
