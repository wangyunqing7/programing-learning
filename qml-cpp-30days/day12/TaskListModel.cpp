#include "TaskListModel.h"

TaskListModel::TaskListModel(QObject *parent)
    : QAbstractListModel(parent)
{
    m_tasks = {
        {QStringLiteral("理解 roleNames"), false},
        {QStringLiteral("把 C++ 模型绑定到 ListView"), false},
        {QStringLiteral("从 QML 调用模型方法"), true}
    };
}

int TaskListModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid()) {
        return 0;
    }
    return m_tasks.size();
}

QVariant TaskListModel::data(const QModelIndex &index, int role) const
{
    if (!index.isValid() || index.row() < 0 || index.row() >= m_tasks.size()) {
        return {};
    }

    const Task &task = m_tasks.at(index.row());
    if (role == TitleRole) {
        return task.title;
    }
    if (role == DoneRole) {
        return task.done;
    }
    return {};
}

QHash<int, QByteArray> TaskListModel::roleNames() const
{
    return {
        {TitleRole, "title"},
        {DoneRole, "done"}
    };
}

void TaskListModel::addTask(const QString &title)
{
    const QString cleanTitle = title.trimmed();
    if (cleanTitle.isEmpty()) {
        return;
    }

    const int row = m_tasks.size();
    beginInsertRows(QModelIndex(), row, row);
    m_tasks.append({cleanTitle, false});
    endInsertRows();
}

void TaskListModel::toggleDone(int row)
{
    if (row < 0 || row >= m_tasks.size()) {
        return;
    }
    m_tasks[row].done = !m_tasks[row].done;
    const QModelIndex changed = index(row, 0);
    emit dataChanged(changed, changed, {DoneRole});
}

void TaskListModel::removeTask(int row)
{
    if (row < 0 || row >= m_tasks.size()) {
        return;
    }
    beginRemoveRows(QModelIndex(), row, row);
    m_tasks.removeAt(row);
    endRemoveRows();
}
