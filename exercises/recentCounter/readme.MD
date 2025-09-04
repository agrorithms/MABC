Recent Counter
Recent Counter is a class that tracks incoming requests from multiple users over time.
Each request (ping) has a user and a timestamp in ms, and the system will report the number pings from that user in the past N seconds, N is determined at system start. Each ping call should have increasing time stamp
The get_all(user) method can be used to return all ping requests from a given user in the current system regardless of timestamp
Initializing the recent counter has O(1) time and space - does not depend on N
Ping method has O(n) time and space complexity where n is the number of  pings for the given user. This is because each ping adds an element to that user's list, and loops through the list to determine # of pings in past N seconds (does this method have O(n) space complexity or is it the whole class that has this space complexity? each singular ping adds just one element, but # of pings on the class instance determines space needed)
get_all method has O(1) time and space complexity as it only is looking for a value via a key in a hashmap