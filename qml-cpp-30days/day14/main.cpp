#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "JsonStore.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        JsonStore store;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("store", &store);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day14", "Main");
        return app.exec();
    }
