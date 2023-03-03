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

    fn modulus(&self) -> f64 {
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
        return self.conjugate() / (self.modulus() * self.modulus());
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
    let modulus = c1.modulus();
    let inverse = c1.inverse();

    sum.print();
    diff.print();
    mul.print();
    div.print();
    println!("{}", arg);
    println!("{}", modulus);
    inverse.print();
}
