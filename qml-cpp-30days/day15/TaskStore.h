#ifndef TASKSTORE_H
#define TASKSTORE_H

#include <QObject>
#include <QVariantList>

class TaskStore : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QVariantList tasks READ tasks NOTIFY tasksChanged)

public:
    explicit TaskStore(QObject *parent = nullptr);

    QVariantList tasks() const;

    Q_INVOKABLE void addTask(const QString &title);
    Q_INVOKABLE void toggleTask(int row);
    Q_INVOKABLE void removeTask(int row);
    Q_INVOKABLE bool load();
    Q_INVOKABLE bool save() const;

signals:
    void tasksChanged();

private:
    QString filePath() const;
    QVariantList m_tasks;
};

#endif
