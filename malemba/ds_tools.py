class ArrayHandler(object):

    def __init__(self, group_lims=None):
        self.group_lims = group_lims

    def aggregate(self, array, aggr_level, _top_level=True):
        if aggr_level < 1:
            return array
        if self.group_lims is None:
            self.group_lims = [list() for k in range(aggr_level)]
            i = -1
        else:
            try:
                i = self.group_lims[aggr_level - 1][-1]
            except IndexError:
                i = -1
        aggr_array = list()
        if aggr_level == 1:
            for array_elm in array:
                if _top_level:
                    for elm in array_elm:
                        yield elm
                else:
                    aggr_array.extend(array_elm)
                i += len(array_elm)
                self.group_lims[0].append(i)
        else:
            for array_elm in array:
                aggr_array_part = self.aggregate(array=array_elm,
                                                 aggr_level=aggr_level-1,
                                                 _top_level=False)
                if _top_level:
                    for elm in aggr_array_part:
                        yield elm
                else:
                    aggr_array.extend(aggr_array_part)
                i += len(array_elm)
                self.group_lims[aggr_level-1].append(i)

        if not _top_level:
            return aggr_array


def group_array(aggr_array, group_lims):
    if len(group_lims) == 1:
        return _group_level(aggr_array, group_lims.pop(0))
    aggr_array = _group_level(aggr_array, group_lims.pop(0))
    return group_array(aggr_array, group_lims)


def _group_level(aggr_array, level_lims):
    grouped_array = [list()]
    for i in range(len(aggr_array)):
        grouped_array[-1].append(aggr_array[i])
        if i == level_lims[0]:
            level_lims.pop(0)
            grouped_array.append(list())
    return list(filter(None, grouped_array))
