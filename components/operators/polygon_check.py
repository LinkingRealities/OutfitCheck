""" Polygons amount validation """
import bpy

MAX_RANGE_THRESHOLD = 15000  # unacceptable max value
WARNING_RANGE_THRESHOLD = 10000  # warning , but acceptable max value


def calculate_polygons():
    sum_faces = []
    for obj in bpy.data.objects:
        if obj.type != 'MESH':
            continue
        faces = sum(len(polygon.vertices) - 2 for polygon in obj.data.polygons)
        sum_faces.append(faces)
    return sum(sum_faces)


def execute_polygon_check():
    try:
        summa = calculate_polygons()
        if summa <= 0:
            return False, "There are no polygons in the scene. Please fix it"

        elif summa >= MAX_RANGE_THRESHOLD:
            return False, f"Polygons amount exceeds {MAX_RANGE_THRESHOLD}. Please reduce it to be able to export"

        elif WARNING_RANGE_THRESHOLD < summa < MAX_RANGE_THRESHOLD:
            return True, f"Polygons amount in range [{WARNING_RANGE_THRESHOLD}: {MAX_RANGE_THRESHOLD}]. It's acceptable"

        elif 0 <= summa <= WARNING_RANGE_THRESHOLD:
            return True, f"Polygons amount is less than {WARNING_RANGE_THRESHOLD}. It's acceptable"

    except Exception as exc:
        print("ERROR: Can't count polygons: ", exc)
