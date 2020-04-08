# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotMPolar
        A SlotMPolar object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    # Computation of isthmus surface
    if self.is_outwards():
        # Surface of the external disk
        Sext = ((self.H0 + Rbo) ** 2) * pi

        # Surface of the internal disk
        Sint = (Rbo ** 2) * pi
    else:
        # Surface of the external disk
        Sext = (Rbo ** 2) * pi

        # Surface of the internal disk
        Sint = ((Rbo - self.H0) ** 2) * pi
    # Surface of the ring
    Sring = Sext - Sint

    # Only an W0 angle of the ring
    return Sring * self.W0 / (2 * pi)
