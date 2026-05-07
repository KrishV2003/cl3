# Class for fuzzy set operations
class FuzzySet:

    # Constructor
    def __init__(self, set_elements):

        self.set_elements = set_elements

    # Union operation
    def union(self, other):

        result = {}

        for key in set(self.set_elements.keys()).union(other.set_elements.keys()):

            result[key] = max(
                self.set_elements.get(key, 0),
                other.set_elements.get(key, 0)
            )

        return FuzzySet(result)

    # Intersection operation
    def intersection(self, other):

        result = {}

        for key in set(self.set_elements.keys()).intersection(other.set_elements.keys()):

            result[key] = min(
                self.set_elements.get(key, 0),
                other.set_elements.get(key, 0)
            )

        return FuzzySet(result)

    # Complement operation
    def complement(self):

        result = {}

        for key, value in self.set_elements.items():

            result[key] = 1 - value

        return FuzzySet(result)

    # Difference operation
    def difference(self, other):

        result = {}

        for key in self.set_elements:

            result[key] = min(
                self.set_elements[key],
                1 - other.set_elements.get(key, 0)
            )

        return FuzzySet(result)


# Class for fuzzy relations
class FuzzyRelation:

    # Cartesian product
    @staticmethod
    def cartesian_product(set1, set2):

        result = {}

        for k1, v1 in set1.set_elements.items():

            for k2, v2 in set2.set_elements.items():

                result[(k1, k2)] = min(v1, v2)

        return result

    # Max-Min Composition
    @staticmethod
    def max_min_composition(relation1, relation2):

        result = {}

        keys1 = set(x[0] for x in relation1.keys())

        keys2 = set(x[1] for x in relation2.keys())

        for k1 in keys1:

            for k2 in keys2:

                values = []

                for x in keys2:

                    if (k1, x) in relation1 and (x, k2) in relation2:

                        values.append(
                            min(
                                relation1[(k1, x)],
                                relation2[(x, k2)]
                            )
                        )

                if values:
                    result[(k1, k2)] = max(values)

        return result


# Define fuzzy sets
fuzzy_set1 = FuzzySet({
    'a': 0.5,
    'b': 0.7,
    'c': 0.2
})

fuzzy_set2 = FuzzySet({
    'a': 0.6,
    'b': 0.3,
    'c': 0.8,
    'd': 0.5
})

# Perform operations
union_result = fuzzy_set1.union(fuzzy_set2)

intersection_result = fuzzy_set1.intersection(fuzzy_set2)

complement_result = fuzzy_set1.complement()

difference_result = fuzzy_set1.difference(fuzzy_set2)

# Fuzzy relations
relation1 = FuzzyRelation.cartesian_product(
    fuzzy_set1,
    fuzzy_set2
)

relation2 = FuzzyRelation.cartesian_product(
    fuzzy_set2,
    fuzzy_set1
)

# Max-Min composition
max_min_result = FuzzyRelation.max_min_composition(
    relation1,
    relation2
)

# Display results
print("Union :", union_result.set_elements)

print("Intersection :", intersection_result.set_elements)

print("Complement :", complement_result.set_elements)

print("Difference :", difference_result.set_elements)

print("Max-Min Composition :", max_min_result)