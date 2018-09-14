from scoring_engine.models.setting import Setting

from tests.scoring_engine.unit_test import UnitTest


class TestSetting(UnitTest):

    def test_init_setting(self):
        setting = Setting(name='test_setting', value='test value example')
        assert setting.id is None
        assert setting.name == 'test_setting'
        assert setting.value == 'test value example'
        self.session.add(setting)
        self.session.commit()
        assert setting.id is not None

    def test_get_setting(self):
        setting_old = Setting(name='test_setting', value='test value example')
        self.session.add(setting_old)
        setting_new = Setting(name='test_setting', value='updated example')
        self.session.add(setting_new)
        self.session.commit()
        assert Setting.get_setting('test_setting').value == 'updated example'

    def test_boolean_value(self):
        setting = Setting(name='test_setting', value=True)
        assert setting.name == 'test_setting'
        assert setting.value is True
        self.session.add(setting)
        self.session.commit()
        assert setting.value is True