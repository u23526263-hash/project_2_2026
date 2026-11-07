import math, unittest
import david_plumb_epq as e, david_plumb_abc as a

class T(unittest.TestCase):
    def test_epq_example(self):
        q = e.calculate_epq(12000, 50, 2, 40, 100)
        self.assertAlmostEqual(q, 1000.0)
        self.assertAlmostEqual(12000 / q, 12.0)
        self.assertAlmostEqual(q / 100, 10.0)
        self.assertAlmostEqual(q * 0.6, 600.0)
    def test_epq_faster(self):
        self.assertLess(e.calculate_epq(12000, 50, 2, 40, 150), 1000)
    def test_epq_to_eoq(self):
        self.assertAlmostEqual(e.calculate_epq(12000, 50, 2, 40, 100000),
                               e.calculate_eoq(12000, 50, 2), delta=0.2)
    def test_epq_bad(self):
        with self.assertRaises(ValueError): e.calculate_epq(1, 1, 1, 100, 100)
    def test_abc_example(self):
        r = a.classify_inventory(a.skus)
        self.assertEqual([i["sku"] for i in r], ["BRK-100","BRG-330","GSK-220","MTR-700","BLT-010","SEAL-500","WSH-050","CBL-900"])
        self.assertEqual([round(i["cum_pct"],1) for i in r], [32.4,49.6,65.8,80.2,87.4,92.8,96.4,100.0])
        self.assertEqual("".join(i["tier"] for i in r), "AAABBBCC")
        self.assertEqual(a.count_tiers(r), {"A":3,"B":3,"C":2})
        self.assertNotIn("value", a.skus[0])  # input untouched
    def test_abc_7090(self):
        self.assertEqual(a.count_tiers(a.classify_inventory(a.skus,70,90)), {"A":3,"B":2,"C":3})

unittest.main(verbosity=2)
