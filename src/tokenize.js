import fs from 'fs/promises';
import path from 'path';

// Función para limpiar texto
function cleanText(text) {
  return text
    .toLowerCase()
    .replace(/[^\w\s]/g, '') // Quita la puntuación
    .replace(/\s+/g, ' ')    // Reemplaza multiples espacios con solo uno
    .trim();
}

// Función para generar n-gramas en el texto
function generateNGrams(text, n) {
  const words = text.split(' ');
  const ngrams = [];
  
  for (let i = 0; i <= words.length - n; i++) {
    ngrams.push(words.slice(i, i + n).join(' '));
  }
  
  return ngrams;
}

// Función principal para procesar los documentos
async function processDocuments(folderPath, ngramSize) {
  try {
    // Crear documentos en el folder si no existe
    try {
      await fs.mkdir(folderPath, { recursive: true });
      console.log(`Folder "${folderPath}" fue creado o ya existe.`);
    } catch (err) {
      console.error(`Error al crear folder: ${err.message}`);
    }
    
    // Leer todos los archivos en el folder
    const files = await fs.readdir(folderPath);
    const textFiles = files.filter(file => path.extname(file).toLowerCase() === '.txt');
    
    if (textFiles.length === 0) {
      console.log('No se encontraron archivos de texto en el folder. Añade algunos archivos .txt');
      return {};
    }
    
    console.log(`Se busco ${textFiles.length} archivos de texto.`);
    
    // Procesar cada archivo
    const documentsData = {};
    
    for (const file of textFiles) {
      const filePath = path.join(folderPath, file);
      const content = await fs.readFile(filePath, 'utf8');
      
      // Limpiar texto
      const cleanedText = cleanText(content);
      
      // Generar n-gramas
      const ngrams = generateNGrams(cleanedText, ngramSize);
      
      // Mostrar resultados
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

// Ejemplo de uso
const folderPath = './documentos';
const ngramSize = 3; // For tri-grams (change to 2 for bi-grams)

// Proceso de documentos para ampliar datos
processDocuments(folderPath, ngramSize).then(documentsData => {
  console.log('\nProcesamiento completado!');
  
  // Mostrar los datos procesados
  for (const [filename, data] of Object.entries(documentsData)) {
    console.log(`\nFile: ${filename}`);
    console.log(`Longitud original: ${data.originalText.length} caracteres`);
    console.log(`Longitud limpio: ${data.cleanedText.length} caracteres`);
    console.log(`Numero de ${ngramSize}-gramas: ${data.ngrams.length}`);
    
    // Mostrar algunos datos de n-gramas
    if (data.ngrams.length > 0) {
      console.log(`Sample ${ngramSize}-grams:`);
      const sampleSize = Math.min(5, data.ngrams.length);
      for (let i = 0; i < sampleSize; i++) {
        console.log(`  - "${data.ngrams[i]}"`);
      }
    }
  }
});