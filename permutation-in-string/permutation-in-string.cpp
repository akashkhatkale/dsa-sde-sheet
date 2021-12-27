class Solution
{
public:
    bool checkInclusion(string s1, string s2)
    {
        if (s1.size() > s2.size())
        {
            return false;
        }

        vector<int> s1Count(26, 0);
        vector<int> s2Count(26, 0);

        for (int i = 0; i < s1.size(); i++)
        {
            s1Count[int(s1[i]) - int('a')] += 1;
            s2Count[int(s2[i]) - int('a')] += 1;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++)
        {
            if (s1Count[i] == s2Count[i])
            {
                matches += 1;
            }
        }

        int left = 0;
        for (int right = s1.size(); right < s2.size(); right++)
        {
            if (matches == 26)
            {
                return true;
            }

            int index = int(s2[right]) - int('a');
            s2Count[index] += 1;
            if (s1Count[index] == s2Count[index])
            {
                matches += 1;
            }
            else if (s1Count[index] + 1 == s2Count[index])
            {
                matches -= 1;
            }

            index = int(s2[left]) - int('a');
            s2Count[index] -= 1;
            if (s1Count[index] == s2Count[index])
            {
                matches += 1;
            }
            else if (s1Count[index] - 1 == s2Count[index])
            {
                matches -= 1;
            }

            left += 1;
        }

        if (matches == 26)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};