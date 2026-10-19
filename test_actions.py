from actions import calculate_similarity, find_matches, build_comparison_summary

def test_calculate_similarity():
    # Test case 1: Caso normal
    data = {"count_total_matches": 5, "total_unique_words": 10}
    assert calculate_similarity(data) == 50.0

    # Test case 2: Cero palabras únicas
    data = {"count_total_matches": 5, "total_unique_words": 0}
    assert calculate_similarity(data) == 0.0

    # Test case 3: No matches
    data = {"count_total_matches": 0, "total_unique_words": 10}
    assert calculate_similarity(data) == 0.0

def test_find_matches():
    # Test case 1: Caso normal
    text1 = ["manzana", "banana", "cereza"]
    text2 = ["banana", "cereza", "fecha"]
    result = find_matches(text1, text2)
    assert result["matches"] == {"banana", "cereza"}
    assert result["only_text1"] == {"manzana"}
    assert result["only_text2"] == {"fecha"}
    assert result["count_total_matches"] == 2
    assert result["list_unique_words"] == {"manzana", "banana", "cereza", "fecha"}
    assert result["total_unique_words"] == 4

    # Test case 2: Sin matches
    text1 = ["manzana", "banana"]
    text2 = ["cereza", "fecha"]
    result = find_matches(text1, text2)
    assert result["matches"] == set()
    assert result["only_text1"] == {"manzana", "banana"}
    assert result["only_text2"] == {"cereza", "fecha"}
    assert result["count_total_matches"] == 0
    assert result["list_unique_words"] == {"manzana", "banana", "cereza", "fecha"}
    assert result["total_unique_words"] == 4

    # Test case 3: todos matches
    text1 = ["manzana", "banana"]
    text2 = ["manzana", "banana"]
    result = find_matches(text1, text2)
    assert result["matches"] == {"manzana", "banana"}
    assert result["only_text1"] == set()
    assert result["only_text2"] == set()
    assert result["count_total_matches"] == 2
    assert result["list_unique_words"] == {"manzana", "banana"}
    assert result["total_unique_words"] == 2
    
def test_build_comparison_summary():
    matches = {
        "count_total_matches": 3,
        "total_unique_words": 5
    }
    similarity = 60.0
    summary = build_comparison_summary(matches, similarity)
    assert summary == (3, 5, 60.0)