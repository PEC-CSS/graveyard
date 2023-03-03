use std::ops;

#[derive(Clone, Copy)]
struct ComplexNumber {
    real: f64,
    imaginary: f64,
}

impl ComplexNumber {
    fn print(&self) {
        let r = self.real;
        let i = self.imaginary;

        if r == 0.0 {
            println!("i {}", self.imaginary);
            return;
        }

        if i == 0.0 {
            println!("{}", self.real);
            return;
        }

        if i < 0.0 {
            println!("{} - i {}", self.real, self.imaginary.abs());
            return;
        }

        println!("{} + i {}", self.real, self.imaginary);
    }

    fn abs(&self) -> f64 {
        return f64::powf(
            (self.real * self.real) + (self.imaginary * self.imaginary),
            0.5,
        );
    }

    fn conjugate(&self) -> ComplexNumber {
        let i = self.imaginary * -1.0;
        return ComplexNumber {
            real: self.real,
            imaginary: i,
        };
    }

    fn argument(&self) -> f64 {
        return f64::atan(self.imaginary / self.real);
    }

    fn inverse(&self) -> ComplexNumber {
        return self.conjugate() / (self.abs() * self.abs());
    }
}

impl ops::Add<&ComplexNumber> for &ComplexNumber {
    type Output = ComplexNumber;
    fn add(self, rhs: &ComplexNumber) -> Self::Output {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        return ComplexNumber {
            real: r1 + r2,
            imaginary: i1 + i2,
        };
    }
}

impl ops::Add<ComplexNumber> for ComplexNumber {
    type Output = ComplexNumber;
    fn add(self, rhs: ComplexNumber) -> Self::Output {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        return ComplexNumber {
            real: r1 + r2,
            imaginary: i1 + i2,
        };
    }
}

impl ops::AddAssign<ComplexNumber> for ComplexNumber {
    fn add_assign(&mut self, rhs: ComplexNumber) {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        *self = ComplexNumber {
            real: r1 + r2,
            imaginary: i1 + i2,
        };
    }
}

impl ops::AddAssign<&ComplexNumber> for ComplexNumber {
    fn add_assign(&mut self, rhs: &ComplexNumber) {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        *self = ComplexNumber {
            real: r1 + r2,
            imaginary: i1 + i2,
        };
    }
}

impl ops::Sub<ComplexNumber> for ComplexNumber {
    type Output = ComplexNumber;
    fn sub(self, rhs: ComplexNumber) -> Self::Output {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        return ComplexNumber {
            real: r1 - r2,
            imaginary: i1 - i2,
        };
    }
}

impl ops::Sub<&ComplexNumber> for &ComplexNumber {
    type Output = ComplexNumber;
    fn sub(self, rhs: &ComplexNumber) -> Self::Output {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        return ComplexNumber {
            real: r1 - r2,
            imaginary: i1 - i2,
        };
    }
}

impl ops::SubAssign<ComplexNumber> for ComplexNumber {
    fn sub_assign(&mut self, rhs: ComplexNumber) {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        *self = ComplexNumber {
            real: r1 - r2,
            imaginary: i1 - i2,
        };
    }
}

impl ops::SubAssign<&ComplexNumber> for ComplexNumber {
    fn sub_assign(&mut self, rhs: &ComplexNumber) {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        *self = ComplexNumber {
            real: r1 - r2,
            imaginary: i1 - i2,
        };
    }
}

impl ops::Mul<ComplexNumber> for ComplexNumber {
    type Output = ComplexNumber;
    fn mul(self, rhs: ComplexNumber) -> Self::Output {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        return ComplexNumber {
            real: r1 * r2 - i1 * i2,
            imaginary: r1 * i2 + r2 * i1,
        };
    }
}

impl ops::Mul<&ComplexNumber> for &ComplexNumber {
    type Output = ComplexNumber;
    fn mul(self, rhs: &ComplexNumber) -> Self::Output {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        return ComplexNumber {
            real: r1 * r2 - i1 * i2,
            imaginary: r1 * i2 + r2 * i1,
        };
    }
}

impl ops::MulAssign<ComplexNumber> for ComplexNumber {
    fn mul_assign(&mut self, rhs: ComplexNumber) {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        *self = ComplexNumber {
            real: r1 * r2 - i1 * i2,
            imaginary: r1 * i2 + r2 * i1,
        };
    }
}

impl ops::MulAssign<&ComplexNumber> for ComplexNumber {
    fn mul_assign(&mut self, rhs: &ComplexNumber) {
        let r1 = self.real;
        let i1 = self.imaginary;
        let r2 = rhs.real;
        let i2 = rhs.imaginary;

        *self = ComplexNumber {
            real: r1 * r2 - i1 * i2,
            imaginary: r1 * i2 + r2 * i1,
        };
    }
}

impl ops::Div<f64> for ComplexNumber {
    type Output = ComplexNumber;
    fn div(self, rhs: f64) -> Self::Output {
        return ComplexNumber {
            real: self.real / rhs,
            imaginary: self.imaginary / rhs,
        };
    }
}

impl ops::Div<f64> for &ComplexNumber {
    type Output = ComplexNumber;
    fn div(self, rhs: f64) -> Self::Output {
        return ComplexNumber {
            real: self.real / rhs,
            imaginary: self.imaginary / rhs,
        };
    }
}

impl ops::Div<ComplexNumber> for ComplexNumber {
    type Output = ComplexNumber;
    fn div(self, rhs: ComplexNumber) -> Self::Output {
        let r2 = rhs.real;
        let i2 = rhs.imaginary;
        let denominator = r2 * r2 + i2 * i2;
        let numerator = self * rhs.conjugate();

        return numerator / denominator;
    }
}

impl ops::Div<&ComplexNumber> for &ComplexNumber {
    type Output = ComplexNumber;
    fn div(self, rhs: &ComplexNumber) -> Self::Output {
        let r2 = rhs.real;
        let i2 = rhs.imaginary;
        let denominator = r2 * r2 + i2 * i2;
        let numerator = self * &rhs.conjugate();

        return numerator / denominator;
    }
}

impl ops::DivAssign<ComplexNumber> for ComplexNumber {
    fn div_assign(&mut self, rhs: ComplexNumber) {
        let r2 = rhs.real;
        let i2 = rhs.imaginary;
        let denominator = r2 * r2 + i2 * i2;
        let numerator = *self * rhs.conjugate();

        *self = numerator / denominator;
    }
}

impl ComplexNumber {
    fn pow(&self, exp: f64) -> ComplexNumber {
        let abs = self.abs();
        let arg = self.argument();
        
        if abs == 0.0 {
            return ComplexNumber {
                real: 0.0,
                imaginary: 0.0,
            };
        }
        let theta = exp * arg;
        let r = f64::powf(abs, exp);

        // TODO
        return ComplexNumber {
            real: r * f64::cos(theta),
            imaginary: r * f64::sin(theta),
        };
    }

    fn cpow(&self, exp: ComplexNumber) -> ComplexNumber {
        let x = exp.real;
        let y = exp.imaginary;

        let abs = self.abs();
        if abs == 0.0 {
            return ComplexNumber {
                real: 0.0,
                imaginary: 0.0,
            };
        }
        let arg = self.argument();
        let mut r = f64::powf(abs, x);
        let mut theta = x * arg;

        if y != 0.0 {
            r *= f64::exp(-y * arg);
            theta += y * f64::ln(abs);
        }

        return ComplexNumber {
            real: r * f64::cos(theta),
            imaginary: r * f64::sin(theta),
        };
    }
}

fn main() {
    let c1 = ComplexNumber {
        real: 4.0,
        imaginary: -8.0,
    };
    let c2 = ComplexNumber {
        real: 2.0,
        imaginary: -1.0,
    };
    let sum = &c1 + &c1;
    let diff = &c1 - &c2;
    let mul = &c1 * &c2;
    let div = &c1 / &c2;
    let arg = c1.argument();
    let abs = c1.abs();
    let inverse = c1.inverse();
    let cpow = c1.cpow(c2);
    let pow = c1.pow(2.0);

    c1.print();
    c2.print();
    sum.print();
    diff.print();
    mul.print();
    div.print();
    println!("{}", arg);
    println!("{}", abs);
    inverse.print();
    cpow.print();
    pow.print();
}
