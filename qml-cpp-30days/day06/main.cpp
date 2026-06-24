#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "MessageProvider.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        MessageProvider messageProvider;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("messageProvider", &messageProvider);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day06", "Main");
        return app.exec();
    }
