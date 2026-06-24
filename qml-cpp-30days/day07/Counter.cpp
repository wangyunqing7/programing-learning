#include "Counter.h"

Counter::Counter(QObject *parent)
    : QObject(parent)
{
}

int Counter::value() const
{
    return m_value;
}

void Counter::setValue(int value)
{
    if (m_value == value) {
        return;
    }
    m_value = value;
    emit valueChanged();
}

void Counter::increase()
{
    setValue(m_value + 1);
}

void Counter::decrease()
{
    setValue(m_value - 1);
}

void Counter::reset()
{
    setValue(0);
}
