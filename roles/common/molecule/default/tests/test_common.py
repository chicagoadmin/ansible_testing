import testinfra


def test_users(host):
  assert host.user('testuser1').exists
  assert host.user('testuser2').exists
  assert host.user('nonadmin1').exists