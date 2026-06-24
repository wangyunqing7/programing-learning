#include <QCoreApplication>
    #include <QGuiApplication>
    #include <QObject>
    #include <QQmlApplicationEngine>
    #include <QQmlContext>
#include "Calculator.h"

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);
        Calculator calculator;

        QQmlApplicationEngine engine;
        engine.rootContext()->setContextProperty("calculator", &calculator);

        QObject::connect(
            &engine,
            &QQmlApplicationEngine::objectCreationFailed,
            &app,
            []() { QCoreApplication::exit(-1); },
            Qt::QueuedConnection);

        engine.loadFromModule("Day09", "Main");
        return app.exec();
    }
