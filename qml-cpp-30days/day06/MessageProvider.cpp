#include "MessageProvider.h"

MessageProvider::MessageProvider(QObject *parent)
    : QObject(parent)
{
}

QString MessageProvider::greeting(const QString &name) const
{
    const QString trimmed = name.trimmed();
    if (trimmed.isEmpty()) {
        return QStringLiteral("你好，QML 学习者。");
    }
    return QStringLiteral("你好，%1。这个字符串来自 C++。").arg(trimmed);
}

QString MessageProvider::todayTopic() const
{
    return QStringLiteral("今天练习 QML 调用 C++ 对象的方法。");
}
