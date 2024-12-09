import sys


def part1(lines: list[str]) -> int:
    expanded_disk = expand_disk(parse_disk(lines))
    return calc_checksum(optimise_disk(expanded_disk))


def parse_disk(lines: str) -> list[(str, int, int)]:
    disk = []
    file_index = 0
    for index, number in enumerate(lines[0]):
        if index % 2 == 0:
            disk.append(("file", int(number), file_index))
            file_index = file_index + 1
        else:
            disk.append(("space", int(number), file_index))

    return disk


def expand_disk(disk: list[(str, int, int)]) -> list[str]:
    expanded_disk = []
    file_index = 0
    for descriptor in disk:
        if descriptor[0] == "file":
            for x in range(descriptor[1]):
                expanded_disk.append(str(file_index))
            file_index = file_index + 1
        else:
            for x in range(descriptor[1]):
                expanded_disk.append(".")

    return expanded_disk


def optimise_disk(disk: list[str]) -> list[str]:
    clean_disk = []
    right_seeker = len(disk) - 1
    for index, content in enumerate(disk):
        if right_seeker < index:
            break

        if content == ".":
            clean_disk.append(disk[right_seeker])
            right_seeker = right_seeker - 1
            while disk[right_seeker] == ".":
                right_seeker = right_seeker - 1
                # print(disk[right_seeker])
        else:
            clean_disk.append(content)

    return clean_disk


def calc_checksum(disk: list[str]) -> int:
    checksum = 0
    for index, content in enumerate(disk):
        checksum = checksum + (index * int(content))

    return checksum


def part2(lines: list[str]) -> int:
    optimised_disk = optimise_disk_full_files(parse_disk(lines))
    # print(optimised_disk)
    return calc_checksum_full_files(optimised_disk)


def optimise_disk_full_files(disk: list[(str, int, int)]) -> list[str]:
    files = list(filter(lambda descriptor: descriptor[0] == "file", disk))
    optimised_disk = disk[:]
    for file in list(reversed(files)):
        file_length = file[1]
        file_index = file[2]
        # print(file_index)
        try:
            fill_space = next(
                descriptor
                for descriptor in optimised_disk
                if descriptor[0] == "space"
                and descriptor[2] <= file_index
                and descriptor[1] >= file_length
            )
            new_disk = []
            for descriptor in optimised_disk:
                if descriptor == fill_space:
                    new_disk.append(file)
                    new_disk.append(
                        (fill_space[0], fill_space[1] - file_length, fill_space[2])
                    )
                    # print("moving file")
                    # print(file)
                elif descriptor == file:
                    new_disk.append(("space", file_length, file_index))
                else:
                    new_disk.append(descriptor)
            # print(new_disk)
            optimised_disk = new_disk
        except StopIteration:
            continue
    return optimised_disk


def calc_checksum_full_files(disk: list[(str, int, int)]) -> int:
    checksum = 0
    disk_index = 0
    for descriptor in disk:
        descriptor_type = descriptor[0]
        file_length = descriptor[1]
        file_index = descriptor[2]
        for x in range(file_length):
            if descriptor_type == "file":
                checksum = checksum + (disk_index * file_index)
                # print(disk_index * file_index)
            disk_index = disk_index + 1

    return checksum
