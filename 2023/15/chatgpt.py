# https://chat.openai.com/share/3403ee8a-dd4d-4737-8378-435775b05f14

import sys


def hash_algorithm(s):
    """Computes the HASH algorithm on a string."""
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value


def combined_hash_and_hashmap(file_path):
    """Reads the initialization sequence from the file and calculates the HASH and HASHMAP results."""
    with open(file_path, "r") as file:
        init_sequence = file.read().strip()

    # Initialize variables for HASH sum and box configuration for HASHMAP
    hash_sum = 0
    boxes = {i: [] for i in range(256)}

    for step in init_sequence.split(","):
        # Perform HASH algorithm on the label
        label = "".join(filter(str.isalpha, step))
        box_number = hash_algorithm(label)
        operation = step[len(label)]

        if operation == "-":
            # Remove the lens with the given label if present
            boxes[box_number] = [
                lens for lens in boxes[box_number] if lens[0] != label
            ]
        else:
            # Add or replace the lens
            focal_length = int(step[len(label) + 1 :])
            lens_present = False

            # Check if lens with same label is already in the box
            for i, lens in enumerate(boxes[box_number]):
                if lens[0] == label:
                    boxes[box_number][i] = (label, focal_length)
                    lens_present = True
                    break

            if not lens_present:
                # Add the lens to the box
                boxes[box_number].append((label, focal_length))

        # Add the HASH result to the sum
        hash_sum += box_number

    # Calculate the focusing power after all steps
    focusing_power = 0
    for box, lenses in boxes.items():
        for slot, (lens_label, lens_focal_length) in enumerate(
            lenses, start=1
        ):
            focusing_power += (box + 1) * slot * lens_focal_length

    return hash_sum, focusing_power


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    hash_sum, focusing_power = combined_hash_and_hashmap(input_file_path)
    print(f"Sum of all hashes: {hash_sum}")
    print(f"Focusing power of the lens configuration: {focusing_power}")
