def comparever( version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    for i in range(max(len(v1), len(v2))):
        gap = (int(v1[i]) if i < len(v1) else 0) - (int(v2[i]) if i < len(v2) else 0)
        if gap != 0:
            return 1 if gap > 0 else -1
    return 0


if __name__ == '__main__':
    print(comparever('1.5.1', '1.5'))
    print(comparever('1.1.0', '1.1'))
    print(comparever('1.5.9.9', '1.5.9.9.9'))
