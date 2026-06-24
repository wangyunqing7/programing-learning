#include "Calculator.h"

Calculator::Calculator(QObject *parent)
    : QObject(parent)
{
}

double Calculator::calculate(double left, double right, const QString &op) const
{
    if (op == QStringLiteral("+")) {
        return left + right;
    }
    if (op == QStringLiteral("-")) {
        return left - right;
    }
    if (op == QStringLiteral("*")) {
        return left * right;
    }
    if (op == QStringLiteral("/") && right != 0.0) {
        return left / right;
    }
    return 0.0;
}
