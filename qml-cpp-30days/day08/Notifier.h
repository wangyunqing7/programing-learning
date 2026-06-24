#ifndef NOTIFIER_H
#define NOTIFIER_H

#include <QObject>
#include <QString>

class Notifier : public QObject
{
    Q_OBJECT
public:
    explicit Notifier(QObject *parent = nullptr);

    Q_INVOKABLE void sendNotice(const QString &text);

signals:
    void notice(const QString &message);
};

#endif
