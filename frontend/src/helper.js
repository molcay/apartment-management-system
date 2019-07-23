const tr_to_ascii_map = {
  'Ö': 'O',
  'ö': 'o',
  'İ': 'I',
  'ı': 'i',
  'Ü': 'U',
  'ü': 'u',
  'Ç': 'C',
  'ç': 'c',
  'Ğ': 'G',
  'ğ': 'g',
  'Ş': 'S',
  'ş': 's',
}

export const tr_to_ascii = (text) => {
  return text.replace(/(([ÖöİıÜüÇçĞğŞş]))/g, letter => tr_to_ascii_map[letter])
}
