from unidiff import PatchSet

class FilesChangedNumber:

    @staticmethod
    def get_num_files_changed(issue):
        diff = issue
        #encoding = diff.headers.get_charsets()[0]
        patch = PatchSet(diff)#, encoding=encoding)
        return len(patch)

    @staticmethod
    def get_num_lines_changed(issue):
        diff = issue
        #encoding = diff.headers.get_charsets()[0]
        patch = PatchSet(diff)#, encoding=encoding)
        count = []
        for p in patch:
            num = p.added + p.removed
            if num is not None:
                count.append(num)
        return sum(count)

