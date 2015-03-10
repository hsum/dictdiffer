#coding=utf-8
"""
A dictionary difference calculator
Originally posted as:
http://stackoverflow.com/questions/1165352/fast-comparison-between-two-python-dictionary/1165552#1165552
"""


class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """
    def __init__(
        self,
        current_dict,
        past_dict,
        report_format = "{key} == {value}",
        report_format_changed = "{key} == {value_old} -> {value_new}",
    ):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.current_keys, self.past_keys = [
            set(d.keys()) for d in (current_dict, past_dict)
        ]
        self.intersect = self.current_keys.intersection(self.past_keys)
        self.report_format = report_format
        self.report_format_changed = report_format_changed

    def added(self):
        return self.current_keys - self.intersect

    def removed(self):
        return self.past_keys - self.intersect

    def changed(self):
        return set(o for o in self.intersect
                   if self.past_dict[o] != self.current_dict[o])

    def unchanged(self):
        return set(o for o in self.intersect
                   if self.past_dict[o] == self.current_dict[o])

    def report_added(self):
        return (self.report_format.format(
            key = key, value = self.current_dict[key]
        ) for key in self.added())

    def report_removed(self):
        return (self.report_format.format(
            key = key, value = self.past_dict[key]
        ) for key in self.removed())

    def report_changed(self):
        return (self.report_format_changed.format(
            key = key,
            value_old = self.past_dict[key],
            value_new = self.current_dict[key],
        ) for key in self.changed())

    def report_unchanged(self):
        return (self.report_format.format(
            key = key, value = self.past_dict[key]
        ) for key in self.unchanged())

