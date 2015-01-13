FILE_EXTENSIONS_TO_SORTS = {
    ".nii,.nii.gz,.nrrd,.png": "PNG",
    '.nii,.nii..gz,.nrrd,.png': 'PNG',
    '.txt,.mat': 'txt',
    '.nii,.nii.gz,.nrrd': 'NRRD',
    '.txt,.mat,.nii,.nii.gz,.nrrd': 'TXT',
    '.nii,.nii.gz,.nrrd,.txt,.mat': "TXT",
}

FLAGS_TYPES = [
    'boolean'
]


DEFAULT_OVERRIDES = {
    'toutputWarpedImageName' : Slot(physical="str")
}

