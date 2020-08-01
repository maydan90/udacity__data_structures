class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.users_set = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)
        self.users_set.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users_set:
        return True
    for gr in group.groups:
        if is_user_in_group(user, gr):
            return True
    return False


parent = Group("parent")
parent.add_user("parent_user")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("parent_user", parent))  # True
print(is_user_in_group("sub_child_user", child))  # True
print(is_user_in_group("parent_user", child))  # False

empty = Group("empty")
print(is_user_in_group("", empty))  # False
print(is_user_in_group("empty", empty))  # False

deep_group = Group('deep')
deep_child = deep_group
for i in range(1000):
    deep_child = Group('deep' + str(i))
    deep_group.add_group(deep_child)
deep_child.add_user('bbb')

print(is_user_in_group("bb", deep_group))  # False
print(is_user_in_group("bbb", deep_group))  # True
