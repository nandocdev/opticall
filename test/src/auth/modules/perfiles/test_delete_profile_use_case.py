#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        test_delete_profile_use_case
# @Date        2025-02-27 13:38:46
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import pytest
from opticall.src.auth.modules.perfiles.application.delete_profile_use_case import DeleteProfileUseCase
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles


def test_delete_profile_success(mock_perfiles_repository, perfil_ejemplo):
    """Prueba que se elimine un perfil correctamente."""
    mock_perfiles_repository.get_by_id.return_value = perfil_ejemplo

    use_case = DeleteProfileUseCase(mock_perfiles_repository)
    use_case.execute(id=1)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.delete_profile.assert_called_once_with(
        perfil_ejemplo)


def test_delete_profile_not_found(mock_perfiles_repository):
    """Prueba que se levante una excepción si no se encuentra el perfil a eliminar."""
    mock_perfiles_repository.get_by_id.return_value = None

    use_case = DeleteProfileUseCase(mock_perfiles_repository)
    with pytest.raises(ValueError, match="No existe un perfil con el ID '1'"):
        use_case.execute(id=1)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.delete_profile.assert_not_called()
