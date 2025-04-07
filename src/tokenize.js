import fs from 'fs/promises';
import path from 'path';

// ====================
// Funciones de Preprocesamiento
// ====================

// Limpia el texto: lo pasa a minúsculas, elimina signos de puntuación y espacios extra.
function cleanText(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s]/g, '') // Quita la puntuación
    .replace(/\s+/g, ' ')    // Reemplaza multiples espacios con uno solo
    .trim();
}

// Genera n-gramas a partir del texto limpio
function generateNGrams(text, n) {
  const words = text.split(' ');
  const ngrams = [];
  for (let i = 0; i <= words.length - n; i++) {
    ngrams.push(words.slice(i, i + n).join(' '));
  }
  return ngrams;
}

// Procesa todos los documentos en el folder dado
async function processDocuments(folderPath, ngramSize) {
  try {
    // Crear folder si no existe
    try {
      await fs.mkdir(folderPath, { recursive: true });
      console.log(`Folder "${folderPath}" fue creado o ya existe.`);
    } catch (err) {
      console.error(`Error al crear folder: ${err.message}`);
    }
    
    // Leer archivos y filtrar los .txt
    const files = await fs.readdir(folderPath);
    const textFiles = files.filter(file => path.extname(file).toLowerCase() === '.txt');
    
    if (textFiles.length === 0) {
      console.log('No se encontraron archivos de texto en el folder. Añade algunos archivos .txt');
      return {};
    }
    
    console.log(`Se encontraron ${textFiles.length} archivos de texto.`);
    
    // Procesar cada archivo
    const documentsData = {};
    for (const file of textFiles) {
      const filePath = path.join(folderPath, file);
      const content = await fs.readFile(filePath, 'utf8');
      const cleanedText = cleanText(content);
      const ngrams = generateNGrams(cleanedText, ngramSize);
      
      documentsData[file] = {
        originalText: content,
        cleanedText: cleanedText,
        ngrams: ngrams,
        ngramCount: ngrams.length
      };
      
      console.log(`Procesando "${file}": ${ngrams.length} ${ngramSize}-gramas generados.`);
    }
    
    return documentsData;
  } catch (error) {
    console.error('Error al procesar documentos:', error);
    return {};
  }
}

// ====================
// Funciones Hash y Comparación
// ====================

// Función hash personalizada simple para los n-gramas
function simpleHash(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = (hash << 5) - hash + str.charCodeAt(i);
    hash |= 0; // Convierte a entero de 32 bits
  }
  return hash;
}

// Crea una tabla hash para cada documento, convirtiendo cada n-grama a su valor hash.
function createHashTables(documentsData) {
  const hashTables = {};
  for (const [filename, data] of Object.entries(documentsData)) {
    const hashSet = new Set();
    for (const ngram of data.ngrams) {
      hashSet.add(simpleHash(ngram));
    }
    hashTables[filename] = hashSet;
  }
  return hashTables;
}

// Calcula la similitud de Jaccard entre dos conjuntos (Sets)
function jaccardSimilarity(setA, setB) {
  const intersection = new Set([...setA].filter(x => setB.has(x)));
  const union = new Set([...setA, ...setB]);
  return union.size === 0 ? 0 : intersection.size / union.size;
}

// Compara cada par de documentos y calcula su similitud usando la Similitud de Jaccard
function compareDocuments(hashTables) {
  const results = [];
  const filenames = Object.keys(hashTables);
  for (let i = 0; i < filenames.length; i++) {
    for (let j = i + 1; j < filenames.length; j++) {
      const fileA = filenames[i];
      const fileB = filenames[j];
      const similarity = jaccardSimilarity(hashTables[fileA], hashTables[fileB]);
      results.push({ fileA, fileB, similarity });
    }
  }
  return results;
}

// ====================
// Funciones de Ordenamiento y Visualización
// ====================

// Implementación de Merge Sort para ordenar los pares según similitud (descendente)
function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));
  return merge(left, right);
}

function merge(left, right) {
  const result = [];
  let i = 0, j = 0;
  while (i < left.length && j < right.length) {
    if (left[i].similarity >= right[j].similarity) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }
  return result.concat(left.slice(i)).concat(right.slice(j));
}

// Muestra los top N pares de documentos con mayor similitud
function showTopResults(results, topN) {
  console.log(`\nTop ${topN} documentos más similares:`);
  const topResults = results.slice(0, topN);
  for (const result of topResults) {
    console.log(`${result.fileA} <--> ${result.fileB} | Similitud: ${result.similarity.toFixed(4)}`);
  }
}

// ====================
// Ejecución Principal
// ====================

const folderPath = './documentos';
const ngramSize = 3; // Cambia a 2 para bi-gramas, o 3 para tri-gramas
const topN = 6;      // Número de pares a mostrar

processDocuments(folderPath, ngramSize)
  .then(documentsData => {
    if (Object.keys(documentsData).length === 0) {
      console.log('No se procesaron documentos.');
      return;
    }
    // Crear tabla hash con los n-gramas de cada documento
    const hashTables = createHashTables(documentsData);
    // Comparar cada par de documentos y calcular la similitud de Jaccard
    const similarityResults = compareDocuments(hashTables);
    // Ordenar los resultados utilizando Merge Sort
    const sortedResults = mergeSort(similarityResults);
    // Mostrar los top N pares con mayor similitud
    showTopResults(sortedResults, topN);
  })
  .catch(err => {
    console.error('Error en la ejecución principal:', err);
  });
