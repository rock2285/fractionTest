class Fraction(object):
  """A rational number represented by an integer numerator and denominator."""

  def __init__(self, numerator=0, denominator=1):
    """Create a fraction and normalize it to lowest terms.

    Preconditions: numerator and denominator are integers; denominator is nonzero.
    Postconditions: numerator and denominator represent the supplied value, share
      no common factor other than 1, and the denominator is positive.
    Side effects: initializes this instance's numerator and denominator.
    Exceptions: TypeError for non-integer arguments; ZeroDivisionError when the
      denominator is zero.
    """

  def __str__(self):
    """Return the fraction in display form.

    Preconditions: this instance represents a valid fraction.
    Postconditions: returns ``n/d``, except that denominator 1 is displayed as ``n``.
    Side effects: none.
    Exceptions: none.
    """

  def __float__(self):
    """Convert this fraction to a floating-point number.

    Preconditions: this instance represents a valid fraction.
    Postconditions: returns the floating-point quotient of numerator by denominator.
    Side effects: none.
    Exceptions: OverflowError if the value cannot be represented as a float.
    """

  def __int__(self):
    """Convert this fraction to an integer by truncating toward zero.

    Preconditions: this instance represents a valid fraction.
    Postconditions: returns the quotient truncated toward zero.
    Side effects: none.
    Exceptions: none.
    """

  def __eq__(self, other):
    """Compare this fraction with another fraction for equality.

    Preconditions: this instance represents a valid fraction.
    Postconditions: returns whether both values are equal; unsupported operand
      types compare unequal.
    Side effects: none.
    Exceptions: none.
    """

  def __ne__(self, other):
    """Compare this fraction with another fraction for inequality.

    Preconditions: this instance represents a valid fraction.
    Postconditions: returns the logical inverse of equality, including True for
      unsupported operand types.
    Side effects: none.
    Exceptions: none.
    """

  def __lt__(self, other):
    """Test whether this fraction is less than another fraction.

    Preconditions: this instance and other are fractions.
    Postconditions: returns whether this value is less than other.
    Side effects: none.
    Exceptions: TypeError if other is not a fraction.
    """

  def __le__(self, other):
    """Test whether this fraction is less than or equal to another fraction.

    Preconditions: this instance and other are fractions.
    Postconditions: returns whether this value is less than or equal to other.
    Side effects: none.
    Exceptions: TypeError if other is not a fraction.
    """

  def __gt__(self, other):
    """Test whether this fraction is greater than another fraction.

    Preconditions: this instance and other are fractions.
    Postconditions: returns whether this value is greater than other.
    Side effects: none.
    Exceptions: TypeError if other is not a fraction.
    """

  def __ge__(self, other):
    """Test whether this fraction is greater than or equal to another fraction.

    Preconditions: this instance and other are fractions.
    Postconditions: returns whether this value is greater than or equal to other.
    Side effects: none.
    Exceptions: TypeError if other is not a fraction.
    """

  def __add__(self, other):
    """Add another fraction or integer to this fraction.

    Preconditions: this instance is valid; other is a fraction or integer.
    Postconditions: returns the exact sum as a normalized fraction.
    Side effects: does not modify either operand.
    Exceptions: TypeError for unsupported operand types.
    """

  
  def __sub__(self, other):
    """Subtract another fraction or integer from this fraction.

    Preconditions: this instance is valid; other is a fraction or integer.
    Postconditions: returns the exact difference as a normalized fraction.
    Side effects: does not modify either operand.
    Exceptions: TypeError for unsupported operand types.
    """

  def __mul__(self, other):
    """Multiply this fraction by another fraction or integer.

    Preconditions: this instance is valid; other is a fraction or integer.
    Postconditions: returns the exact product as a normalized fraction.
    Side effects: does not modify either operand.
    Exceptions: TypeError for unsupported operand types.
    """

  def __truediv__(self, other):
    """Divide this fraction by another fraction or integer.

    Preconditions: this instance is valid; other is a nonzero fraction or integer.
    Postconditions: returns the exact quotient as a normalized fraction.
    Side effects: does not modify either operand.
    Exceptions: TypeError for unsupported operand types; ZeroDivisionError if
      other is zero.
    """


  def __neg__(self):
    """Return the additive inverse of this fraction.

    Preconditions: this instance represents a valid fraction.
    Postconditions: returns a normalized fraction whose sum with this value is zero.
    Side effects: does not modify this instance.
    Exceptions: none.
    """
