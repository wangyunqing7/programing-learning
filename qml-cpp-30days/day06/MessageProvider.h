#ifndef MESSAGEPROVIDER_H
#define MESSAGEPROVIDER_H

#include <QObject>
#include <QString>

class MessageProvider : public QObject
{
    Q_OBJECT
public:
    explicit MessageProvider(QObject *parent = nullptr);

    Q_INVOKABLE QString greeting(const QString &name) const;
    Q_INVOKABLE QString todayTopic() const;
};

#endif
