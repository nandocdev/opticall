#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        test_get_profile_use_case
# @Date        2025-02-27 13:37:19
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import pytest
from opticall.src.auth.modules.perfiles.application.get_profile_use_case import GetProfileUseCase
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles


def test_get_profile_success(mock_perfiles_repository, perfil_ejemplo):
    """Prueba que se obtenga un perfil correctamente por su ID."""
    mock_perfiles_repository.get_by_id.return_value = perfil_ejemplo

    use_case = GetProfileUseCase(mock_perfiles_repository)
    perfil_obtenido = use_case.execute(id=1)

    assert perfil_obtenido == perfil_ejemplo
    mock_perfiles_repository.get_by_id.assert_called_once_with(1)


def test_get_profile_not_found(mock_perfiles_repository):
    """Prueba que se levante una excepción si no se encuentra el perfil."""
    mock_perfiles_repository.get_by_id.return_value = None

    use_case = GetProfileUseCase(mock_perfiles_repository)
    with pytest.raises(ValueError, match="No existe un perfil con el ID '1'"):
        use_case.execute(id=1)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
