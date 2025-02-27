#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        test_update_profile_use_case
# @Date        2025-02-27 13:38:00
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import pytest
from opticall.src.auth.modules.perfiles.application.update_profile_use_case import UpdateProfileUseCase
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles

def test_update_profile_success(mock_perfiles_repository, perfil_ejemplo):
    """Prueba que se actualice un perfil correctamente."""
    mock_perfiles_repository.get_by_id.return_value = perfil_ejemplo
    mock_perfiles_repository.exists_by_name.return_value = False

    use_case = UpdateProfileUseCase(mock_perfiles_repository)
    use_case.execute(id=1, nombre="NuevoNombre",
                     descripcion="NuevaDescripcion", estado=False)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.update_profile.assert_called_once_with(
        Perfiles(id=1, nombre="NuevoNombre", descripcion="NuevaDescripcion", estado=False))


def test_update_profile_not_found(mock_perfiles_repository):
    """Prueba que se levante una excepción si no se encuentra el perfil a actualizar."""
    mock_perfiles_repository.get_by_id.return_value = None

    use_case = UpdateProfileUseCase(mock_perfiles_repository)
    with pytest.raises(ValueError, match="No existe un perfil con el ID '1'"):
        use_case.execute(id=1, nombre="NuevoNombre",
                         descripcion="NuevaDescripcion", estado=False)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.update_profile.assert_not_called()


def test_update_profile_name_already_exists(mock_perfiles_repository, perfil_ejemplo):
    """Prueba que se levante una excepción si ya existe un perfil con el nuevo nombre."""
    mock_perfiles_repository.get_by_id.return_value = perfil_ejemplo
    mock_perfiles_repository.exists_by_name.return_value = True

    use_case = UpdateProfileUseCase(mock_perfiles_repository)
    with pytest.raises(ValueError, match="Ya existe un perfil con el nombre 'NuevoNombre'"):
        use_case.execute(id=1, nombre="NuevoNombre",
                         descripcion="NuevaDescripcion", estado=False)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.update_profile.assert_not_called()
