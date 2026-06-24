#include "JsonStore.h"

#include <QDir>
#include <QFile>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonObject>
#include <QStandardPaths>
#include <QVariantMap>

JsonStore::JsonStore(QObject *parent)
    : QObject(parent)
{
    load();
}

QVariantList JsonStore::items() const
{
    return m_items;
}

bool JsonStore::load()
{
    QFile file(filePath());
    if (!file.exists()) {
        m_items = {
            QVariantMap{{QStringLiteral("title"), QStringLiteral("第一条本地数据")}},
            QVariantMap{{QStringLiteral("title"), QStringLiteral("保存后再次启动仍然存在")}}
        };
        emit itemsChanged();
        return save();
    }

    if (!file.open(QIODevice::ReadOnly)) {
        return false;
    }

    const QJsonDocument document = QJsonDocument::fromJson(file.readAll());
    QVariantList loaded;
    for (const QJsonValue &value : document.array()) {
        loaded.append(value.toObject().toVariantMap());
    }
    m_items = loaded;
    emit itemsChanged();
    return true;
}

bool JsonStore::save() const
{
    const QString path = filePath();
    QDir().mkpath(QFileInfo(path).absolutePath());

    QJsonArray array;
    for (const QVariant &item : m_items) {
        array.append(QJsonObject::fromVariantMap(item.toMap()));
    }

    QFile file(path);
    if (!file.open(QIODevice::WriteOnly | QIODevice::Truncate)) {
        return false;
    }
    file.write(QJsonDocument(array).toJson(QJsonDocument::Indented));
    return true;
}

void JsonStore::addItem(const QString &title)
{
    const QString cleanTitle = title.trimmed();
    if (cleanTitle.isEmpty()) {
        return;
    }
    m_items.append(QVariantMap{{QStringLiteral("title"), cleanTitle}});
    emit itemsChanged();
    save();
}

QString JsonStore::filePath() const
{
    const QString base = QStandardPaths::writableLocation(QStandardPaths::AppDataLocation);
    return base + QStringLiteral("/day14-items.json");
}
