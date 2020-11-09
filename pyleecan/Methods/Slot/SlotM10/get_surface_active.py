# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """

    # get the name of the lamination
    st = self.get_name_lam()

    [_, _, _, _, ZM1, ZM2, ZM3, ZM4] = self._comp_point_coordinate()
    curve_list = list()
    curve_list.append(Segment(ZM1, ZM2))
    curve_list.append(Segment(ZM2, ZM3))
    curve_list.append(Segment(ZM3, ZM4))
    curve_list.append(Segment(ZM4, ZM1))

    Zmid = (ZM1 + ZM3) / 2

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Zmid
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
