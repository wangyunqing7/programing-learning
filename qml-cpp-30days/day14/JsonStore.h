#ifndef JSONSTORE_H
#define JSONSTORE_H

#include <QObject>
#include <QVariantList>

class JsonStore : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QVariantList items READ items NOTIFY itemsChanged)

public:
    explicit JsonStore(QObject *parent = nullptr);

    QVariantList items() const;

    Q_INVOKABLE bool load();
    Q_INVOKABLE bool save() const;
    Q_INVOKABLE void addItem(const QString &title);

signals:
    void itemsChanged();

private:
    QString filePath() const;
    QVariantList m_items;
};

#endif
