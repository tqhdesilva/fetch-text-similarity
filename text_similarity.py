from typing import List
from collections import deque, Counter
import re

_PUNCT_RE = re.compile(r"[.!,-?]")


def _inner_product(v1, v2):
    return sum((i * j for i, j in zip(v1, v2)))


def _cosine_similarity(v1: List[int], v2: List[int]):
    return _inner_product(v1, v2) / (
        _inner_product(v1, v1) ** 0.5 * _inner_product(v2, v2) ** 0.5
    )


def _bow(text: str, n: int) -> Counter:
    bow = Counter()
    n = max(1, n)
    text = _PUNCT_RE.sub(" ", text)
    tokens = [token for token in text.split(" ") if token]
    window = deque()
    for token in tokens:
        window.append(token)
        if len(window) > n:
            window.popleft()
        window_tup = tuple(window)
        for i in range(-1, -n - 1, -1):
            bow[tuple(window_tup[i:])] += 1
    return bow


def similarity(text1: str, text2: str, n: int = 3):
    bow1, bow2 = _bow(text1, n), _bow(text2, n)
    keys = list(set(bow1.keys()).union(set(bow2.keys())))
    vector1, vector2 = [bow1[key] for key in keys], [bow2[key] for key in keys]
    return _cosine_similarity(vector1, vector2)


if __name__ == "__main__":
    # test code
    sample1 = (
        "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. "
        "If you have any participating brands on your receipt, you'll get points based on the cost of the products. "
        "You don't need to clip any coupons or scan individual barcodes. "
        "Just scan each grocery receipt after you shop and we'll find the savings for you."
    )
    sample2 = (
        "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. "
        "If you have any eligible brands on your receipt, you will get points based on the total cost of the products. "
        "You do not need to cut out any coupons or scan individual UPCs. "
        "Just scan your receipt after you check out and we will find the savings for you."
    )
    sample3 = (
        "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. "
        "These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. "
        "No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
    )
    samples = [sample1, sample2, sample3]
    for i in range(3):
        for j in range(i, 3):
            print(
                f"Sample {i + 1}-{j + 1} cosine similarity: {similarity(samples[i], samples[j])}"
            )
