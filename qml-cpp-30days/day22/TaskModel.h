#ifndef TASKMODEL_H
#define TASKMODEL_H

#include <QAbstractListModel>
#include <QString>
#include <QVariantMap>
#include <QVector>

class TaskModel : public QAbstractListModel
{
    Q_OBJECT
    Q_PROPERTY(QString filterText READ filterText WRITE setFilterText NOTIFY filterChanged)
    Q_PROPERTY(QString filterCategory READ filterCategory WRITE setFilterCategory NOTIFY filterChanged)
    Q_PROPERTY(int totalCount READ totalCount NOTIFY countChanged)
    Q_PROPERTY(int visibleCount READ visibleCount NOTIFY countChanged)
    Q_PROPERTY(int completedCount READ completedCount NOTIFY countChanged)

public:
    enum Roles {
        TitleRole = Qt::UserRole + 1,
        NoteRole,
        CategoryRole,
        DoneRole,
        CreatedAtRole
    };

    explicit TaskModel(QObject *parent = nullptr);

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
    QHash<int, QByteArray> roleNames() const override;

    QString filterText() const;
    void setFilterText(const QString &text);
    QString filterCategory() const;
    void setFilterCategory(const QString &category);

    int totalCount() const;
    int visibleCount() const;
    int completedCount() const;

    Q_INVOKABLE QVariantMap get(int row) const;
    Q_INVOKABLE void addTask(const QString &title, const QString &note, const QString &category);
    Q_INVOKABLE void removeTask(int row);
    Q_INVOKABLE void updateTask(int row, const QString &title, const QString &note, const QString &category);
    Q_INVOKABLE void toggleDone(int row);
    Q_INVOKABLE void clearCompleted();
    Q_INVOKABLE bool save() const;
    Q_INVOKABLE bool load();
    Q_INVOKABLE bool exportTo(const QString &fileName) const;
    Q_INVOKABLE bool importFrom(const QString &fileName);

signals:
    void filterChanged();
    void countChanged();

private:
    struct Task {
        QString title;
        QString note;
        QString category;
        bool done = false;
        QString createdAt;
    };

    QVector<Task> m_tasks;
    QVector<int> m_visibleRows;
    QString m_filterText;
    QString m_filterCategory;

    void seed();
    void rebuildVisibleRows();
    int sourceRowForVisibleRow(int row) const;
    QString storagePath() const;
    QString documentPath(const QString &fileName) const;
    QJsonObject toJson(const Task &task) const;
    Task fromJson(const QJsonObject &object) const;
};

#endif
