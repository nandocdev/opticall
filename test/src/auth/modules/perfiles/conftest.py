#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        conftest
# @Date        2025-02-27 13:36:03
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import pytest
from unittest.mock import Mock
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles
from opticall.src.auth.modules.perfiles.domain.interfaces.perfiles_interface import PerfilesInterface


@pytest.fixture
def mock_perfiles_repository():
    """Fixture que crea un mock del repositorio de perfiles."""
    return Mock(spec=PerfilesInterface)


@pytest.fixture
def perfil_ejemplo():
    """Fixture que crea un objeto Perfil de ejemplo."""
    return Perfiles(id=1, nombre="Administrador", descripcion="Perfil de administrador", estado=True)
