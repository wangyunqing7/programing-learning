#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "DataBridge.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        DataBridge bridge;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("bridge", &bridge);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day10", "Main");
        return app.exec();
    }
