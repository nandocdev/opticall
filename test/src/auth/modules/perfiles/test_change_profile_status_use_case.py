#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        test_change_profile_status_use_case
# @Date        2025-02-27 13:39:11
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 
import pytest
from opticall.src.auth.modules.perfiles.application.change_profile_status_use_case import ChangeProfileStatusUseCase
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles


def test_change_profile_status_success(mock_perfiles_repository, perfil_ejemplo):
    """Prueba que se cambie el estado de un perfil correctamente."""
    mock_perfiles_repository.get_by_id.return_value = perfil_ejemplo

    use_case = ChangeProfileStatusUseCase(mock_perfiles_repository)
    use_case.execute(id=1, estado=False)

    assert perfil_ejemplo.estado == False
    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.update_profile.assert_called_once_with(
        perfil_ejemplo)


def test_change_profile_status_not_found(mock_perfiles_repository):
    """Prueba que se levante una excepción si no se encuentra el perfil al que se le cambiará el estado."""
    mock_perfiles_repository.get_by_id.return_value = None

    use_case = ChangeProfileStatusUseCase(mock_perfiles_repository)
    with pytest.raises(ValueError, match="No existe un perfil con el ID '1'"):
        use_case.execute(id=1, estado=False)

    mock_perfiles_repository.get_by_id.assert_called_once_with(1)
    mock_perfiles_repository.update_profile.assert_not_called()
