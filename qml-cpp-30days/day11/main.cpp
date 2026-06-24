#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include <QStringListModel>

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        QStringListModel topicModel(QStringList{QStringLiteral("QML 绑定"), QStringLiteral("C++ 对象"), QStringLiteral("模型视图"), QStringLiteral("JSON 保存")});

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("topicModel", &topicModel);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day11", "Main");
        return app.exec();
    }
