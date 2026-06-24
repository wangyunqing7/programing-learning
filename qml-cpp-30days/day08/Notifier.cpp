#include "Notifier.h"

Notifier::Notifier(QObject *parent)
    : QObject(parent)
{
}

void Notifier::sendNotice(const QString &text)
{
    const QString message = text.trimmed().isEmpty()
        ? QStringLiteral("C++ 发出了一条默认通知")
        : QStringLiteral("C++ 通知：%1").arg(text.trimmed());
    emit notice(message);
}
