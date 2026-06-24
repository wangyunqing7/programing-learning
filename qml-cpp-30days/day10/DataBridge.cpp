#include "DataBridge.h"

#include <QVariantMap>

DataBridge::DataBridge(QObject *parent)
    : QObject(parent)
{
}

QStringList DataBridge::skills() const
{
    return {
        QStringLiteral("QML 属性"),
        QStringLiteral("C++ 方法"),
        QStringLiteral("QVariant 数据")
    };
}

QVariantList DataBridge::tasks() const
{
    QVariantList list;
    list << QVariantMap{{QStringLiteral("title"), QStringLiteral("读取 QVariantList")},
                         {QStringLiteral("level"), QStringLiteral("基础")}};
    list << QVariantMap{{QStringLiteral("title"), QStringLiteral("在 QML 中显示 Map 字段")},
                         {QStringLiteral("level"), QStringLiteral("练习")}};
    list << QVariantMap{{QStringLiteral("title"), QStringLiteral("准备学习模型")},
                         {QStringLiteral("level"), QStringLiteral("进阶")}};
    return list;
}
