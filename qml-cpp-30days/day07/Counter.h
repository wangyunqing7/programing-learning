#ifndef COUNTER_H
#define COUNTER_H

#include <QObject>

class Counter : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int value READ value WRITE setValue NOTIFY valueChanged)

public:
    explicit Counter(QObject *parent = nullptr);

    int value() const;
    void setValue(int value);

    Q_INVOKABLE void increase();
    Q_INVOKABLE void decrease();
    Q_INVOKABLE void reset();

signals:
    void valueChanged();

private:
    int m_value = 0;
};

#endif
