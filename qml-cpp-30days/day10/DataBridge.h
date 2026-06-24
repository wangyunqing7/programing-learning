#ifndef DATABRIDGE_H
#define DATABRIDGE_H

#include <QObject>
#include <QStringList>
#include <QVariantList>

class DataBridge : public QObject
{
    Q_OBJECT
public:
    explicit DataBridge(QObject *parent = nullptr);

    Q_INVOKABLE QStringList skills() const;
    Q_INVOKABLE QVariantList tasks() const;
};

#endif
