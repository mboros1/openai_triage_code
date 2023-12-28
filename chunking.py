import re

def read_document(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def chunk_by_headers(text, header_pattern):
    potential_chunks = re.split(header_pattern, text)
    chunks = []
    for i in range(1, len(potential_chunks), 2):
        chunks.append(potential_chunks[i-1] + potential_chunks[i])
    return chunks

def sort_and_print_chunk_sizes(chunks):
    print(f"There are {len(chunks)} chunks")
    mean_chunk_size = sum(len(chunk) for chunk in chunks) / len(chunks) if chunks else 0
    print(f"Average length of: {mean_chunk_size}")
    chunk_sizes = [len(chunk) for chunk in chunks]
    sorted_chunk_sizes = sorted(chunk_sizes, reverse=True)  # Sort in descending order
    print("The 10 largest chunks are:")
    for size in sorted_chunk_sizes[:10]:  # Print the 10 largest chunk sizes
        print(size)
    
    print("The 10 smallest chunks are:")
    for size in sorted_chunk_sizes[len(sorted_chunk_sizes)-10:]:
        print(size)

def chunk_esi_handbook():
    document_text = read_document('esi-implementation-handbook-2020.txt')
    header_regex = r"Chapter \d+|^\s*[A-Z][A-Z\s]+\s*$"  # Combining chapter and section headers
    return chunk_by_headers(document_text, header_regex)

if __name__ == "__main__":
    sort_and_print_chunk_sizes(chunk_esi_handbook())
