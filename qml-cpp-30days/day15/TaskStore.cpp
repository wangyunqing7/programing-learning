#include "TaskStore.h"

#include <QDir>
#include <QFile>
#include <QFileInfo>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QStandardPaths>
#include <QVariantMap>

TaskStore::TaskStore(QObject *parent)
    : QObject(parent)
{
    load();
}

QVariantList TaskStore::tasks() const
{
    return m_tasks;
}

void TaskStore::addTask(const QString &title)
{
    const QString cleanTitle = title.trimmed();
    if (cleanTitle.isEmpty()) {
        return;
    }
    m_tasks.append(QVariantMap{{QStringLiteral("title"), cleanTitle},
                               {QStringLiteral("done"), false}});
    emit tasksChanged();
    save();
}

void TaskStore::toggleTask(int row)
{
    if (row < 0 || row >= m_tasks.size()) {
        return;
    }
    QVariantMap task = m_tasks.at(row).toMap();
    task[QStringLiteral("done")] = !task.value(QStringLiteral("done")).toBool();
    m_tasks[row] = task;
    emit tasksChanged();
    save();
}

void TaskStore::removeTask(int row)
{
    if (row < 0 || row >= m_tasks.size()) {
        return;
    }
    m_tasks.removeAt(row);
    emit tasksChanged();
    save();
}

bool TaskStore::load()
{
    QFile file(filePath());
    if (!file.exists()) {
        m_tasks = {
            QVariantMap{{QStringLiteral("title"), QStringLiteral("完成第 15 天综合练习")},
                        {QStringLiteral("done"), false}},
            QVariantMap{{QStringLiteral("title"), QStringLiteral("准备进入完整 App 阶段")},
                        {QStringLiteral("done"), false}}
        };
        emit tasksChanged();
        return save();
    }

    if (!file.open(QIODevice::ReadOnly)) {
        return false;
    }
    const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
    QVariantList loaded;
    for (const QJsonValue &value : document.array()) {
        loaded.append(value.toObject().toVariantMap());
    }
    m_tasks = loaded;
    emit tasksChanged();
    return true;
}

bool TaskStore::save() const
{
    const QString path = filePath();
    QDir().mkpath(QFileInfo(path).absolutePath());

    QJsonArray array;
    for (const QVariant &task : m_tasks) {
        array.append(QJsonObject::fromVariantMap(task.toMap()));
    }

    QFile file(path);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
        return false;
    }
    file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
    return true;
}

QString TaskStore::filePath() const
{
    return QStandardPaths::writableLocation(QStandardPaths::AppDataLocation)
        + QStringLiteral("/day15-tasks.json");
}
