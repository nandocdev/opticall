#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @package     auth/modules
# @subpackage  perfiles
# @file        test_list_profiles_use_case
# @Date        2025-02-27 13:37:39
# @Author      Fernando Castillo (ferncastillo@css.gob.pa)
# @Description 

import pytest
from opticall.src.auth.modules.perfiles.application.update_profile_use_case import UpdateProfileUseCase
from opticall.src.auth.modules.perfiles.application.list_profiles_use_case import ListProfilesUseCase
from opticall.src.auth.modules.perfiles.domain.entity.perfiles import Perfiles


def test_list_profiles_success(mock_perfiles_repository, perfil_ejemplo):
    """Prueba que se obtenga una lista de perfiles correctamente."""
    mock_perfiles_repository.get_all.return_value = [perfil_ejemplo]

    use_case = ListProfilesUseCase(mock_perfiles_repository)
    perfiles = use_case.execute()

    assert len(perfiles) == 1
    assert perfiles[0] == perfil_ejemplo
    mock_perfiles_repository.get_all.assert_called_once()
