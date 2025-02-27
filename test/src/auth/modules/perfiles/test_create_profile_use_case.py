#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        test_create_profile_use_case
# @Date        2025-02-27 13:36:18
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import pytest
from opticall.src.auth.modules.perfiles.application.create_profile_use_case import CreateProfileUseCase
from opticall.src.auth.modules.perfiles.infrastructure.repository.mysql_perfiles_repository import MysqlPerfilesRepository
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles


def test_create_profile_success(mock_perfiles_repository):
    """Prueba que la creación de un perfil sea exitosa."""
    perfil = Perfiles(id=1, nombre="NuevoPerfil",
                      descripcion="Descripcion", estado=True)

    mock_perfiles_repository.exists_by_name.return_value = False
    mock_perfiles_repository.create_profile.return_value = perfil

    use_case = CreateProfileUseCase(mock_perfiles_repository)
    perfil_creado = use_case.execute(nombre="NuevoPerfil",
                                     descripcion="Descripcion", estado=True)

    assert perfil_creado == perfil
    mock_perfiles_repository.exists_by_name.assert_called_once_with(
        "NuevoPerfil")
    mock_perfiles_repository.create_profile.assert_called_once_with(perfil)


def test_create_profile_already_exists(mock_perfiles_repository):
    """Prueba que se levante una excepción si ya existe un perfil con el mismo nombre."""
    mock_perfiles_repository.exists_by_name.return_value = True

    use_case = CreateProfileUseCase(mock_perfiles_repository)
    with pytest.raises(ValueError, match="Ya existe un perfil con el nombre 'NuevoPerfil'"):
        use_case.execute(nombre="NuevoPerfil",
                         descripcion="Descripcion", estado=True)

    mock_perfiles_repository.exists_by_name.assert_called_once_with(
        "NuevoPerfil")
    mock_perfiles_repository.create_profile.assert_not_called()
