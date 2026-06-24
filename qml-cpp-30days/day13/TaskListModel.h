#ifndef TASKLISTMODEL_H
#define TASKLISTMODEL_H

#include <QAbstractListModel>
#include <QString>
#include <QVector>

class TaskListModel : public QAbstractListModel
{
    Q_OBJECT
public:
    enum Roles {
        TitleRole = Qt::UserRole + 1,
        DoneRole
    };

    explicit TaskListModel(QObject *parent = nullptr);

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    QHash<int, QByteArray> roleNames() const override;

    Q_INVOKABLE void addTask(const QString &title);
    Q_INVOKABLE void toggleDone(int row);
    Q_INVOKABLE void removeTask(int row);

private:
    struct Task {
        QString title;
        bool done = false;
    };

    QVector<Task> m_tasks;
};

#endif
